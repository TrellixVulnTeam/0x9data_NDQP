// pages/history/history.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    search_date: [],
    sbsbm: [],
    sbzcdm: [],
    dtazdz: [],
    wbdwmc: [],
    sydw: [],
    sydwnbbh: [],
    dtjyjg: [],
    zjyrq: [],
    zjwbrq: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onShow: function () {
    var s1 = new Array();
    var s2 = new Array();
    var s3 = new Array();
    var s4 = new Array();
    var s5 = new Array();
    var s6 = new Array(); 
    var s7 = new Array(); 
    var s8 = new Array();
    var s9 = new Array(); 
    var s10=new Array();
    var keys_cache;
    console.log('fdasfdsf'+typeof(s10));
    console.log(typeof(s1));
    console.log('fdasf'+s1);
    var parse_json=new Array();
    var that=this;
    console.log('fdsaf'+typeof(s2))
    wx.getStorageInfo({
      success: function (res) {
        keys_cache = res.keys;
        console.log('所有的key为' + res.keys)
        console.log(res.currentSize)
        console.log(res.limitSize)
        var key;
        var xx=0;
        for (key in keys_cache) {
          console.log('keys:'+key);
          if (key == '0')
            continue;
          
          wx.getStorage({
            key: key,
            success: function (res) {
              
              console.log('xx:'+xx);
              parse_json[xx] = res.data;
              console.log('data:'+res.data);
              console.log('data_cp:' + parse_json);
              console.log("type"+typeof(s1));
              s1[xx]= key;
              console.log(s1);
              //console.log('fdasfas'+typeof(this.s2));
              s2[xx] = parse_json[xx][0];
              console.log(s2)
              s3[xx] = parse_json[xx][1];
              s4[xx] = parse_json[xx][2];
              s5[xx] = parse_json[xx][3];
              s6[xx] = parse_json[xx][4];
              s7[xx] = parse_json[xx][5];
              s8[xx] = parse_json[xx][6];
              s9[xx] = parse_json[xx][7];
              s10[xx] = parse_json[xx][8];
              that.setData({
                search_date: s1.reverse(),
                sbsbm: s2.reverse(),
                sbzcdm: s3.reverse(),
                dtazdz: s4.reverse(),
                wbdwmc: s5.reverse(),
                sydw: s6.reverse(),
                sydwnbbh: s7.reverse(),
                dtjyjg: s8.reverse(),
                zjyrq: s9.reverse(),
                zjwbrq: s10.reverse(),
                cache_num:xx,
              })
              return  xx+=1;
            }
          })




          }

        }
      })
    console.log(s1);

    // wx.getStorageInfo({
    //   success: function(res){
    //     console.log(res.keys);
    //     keys = res.keys;
    //   }
    // })
    //       var arr = wx.getStorageSync(x);
    //       s1 = s1.unshift(x);
    //}
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */

  onShareAppMessage: function (res) {
    if (res.from === 'button') {
      // 来自页面内转发按钮
      console.log(res.target)
    }
    return {
      title: '自定义转发标题',
      path: '/page/history?id=123',
      success: function (res) {
        // 转发成功
      },
      fail: function (res) {
        // 转发失败
      }
    }
  }
})