from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _

from wagtail.admin.views import generic, mixins
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.core import hooks
from wagtail.users.forms import GroupForm, GroupPagePermissionFormSet

_permission_panel_classes = None


def get_permission_panel_classes():
    global _permission_panel_classes
    if _permission_panel_classes is None:
        _permission_panel_classes = [GroupPagePermissionFormSet]
        for fn in hooks.get_hooks('register_group_permission_panel'):
            _permission_panel_classes.append(fn())

    return _permission_panel_classes


class PermissionPanelFormsMixin:
    def get_permission_panel_form_kwargs(self, cls):
        kwargs = {}

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})

        return kwargs

    def get_permission_panel_forms(self):
        return [
            cls(**self.get_permission_panel_form_kwargs(cls))
            for cls in get_permission_panel_classes()
        ]

    def get_context_data(self, **kwargs):
        if 'permission_panels' not in kwargs:
            kwargs['permission_panels'] = self.get_permission_panel_forms()

        return super().get_context_data(**kwargs)


class IndexView(mixins.SearchableListMixin, generic.IndexView):
    page_title = _("组织")
    add_item_label = _("添加一个组织")
    search_box_placeholder = _("搜索组织")
    search_fields = ['name']
    context_object_name = 'groups'
    paginate_by = 20
    page_kwarg = 'p'
    ordering = ['name']

    def get_template_names(self):
        if self.request.is_ajax():
            return ['wagtailusers/groups/results.html']
        else:
            return ['wagtailusers/groups/index.html']


class CreateView(PermissionPanelFormsMixin, generic.CreateView):
    page_title = _("添加组织")
    success_message = _("已添加 组织：'{0}' .")
    template_name = 'wagtailusers/groups/create.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        # Create an object now so that the permission panel forms have something to link them against
        self.object = Group()

        form = self.get_form()
        permission_panels = self.get_permission_panel_forms()
        if form.is_valid() and all(panel.is_valid() for panel in permission_panels):
            response = self.form_valid(form)

            for panel in permission_panels:
                panel.save()

            return response
        else:
            return self.form_invalid(form)


class EditView(PermissionPanelFormsMixin, generic.EditView):
    success_message = _("已更新组织 ：'{0}' .")
    error_message = _("由于一些错误 该组织不能被保存.")
    delete_item_label = _("删除组织")
    context_object_name = 'group'
    template_name = 'wagtailusers/groups/edit.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()

        form = self.get_form()
        permission_panels = self.get_permission_panel_forms()
        if form.is_valid() and all(panel.is_valid() for panel in permission_panels):
            response = self.form_valid(form)

            for panel in permission_panels:
                panel.save()

            return response
        else:
            return self.form_invalid(form)


class DeleteView(generic.DeleteView):
    success_message = _("已删除组织 '{0}'.")
    page_title = _("删除组织")
    confirmation_message = _("你确定要删除该组?")
    template_name = 'wagtailusers/groups/confirm_delete.html'


class GroupViewSet(ModelViewSet):
    icon = 'group'
    model = Group

    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView

    def get_form_class(self, for_update=False):
        return GroupForm
