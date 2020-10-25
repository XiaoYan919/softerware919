Page({
  data:{
    idH:"H",
    idO:"O",
    idBt:"B",
    idsin:"sin",  //第一排
    idcos:"cos",
    idtan:"tan",
    idasin:"asin",
    idatan:"atan",  //第二排
    idb:"back",
    idc:"clear",
    idt:"toggle",
    idadd:"＋",
    id9:"9",
    id8:"8",
    id7:"7",
    idj:"－",
    id6:"6",
    id5:"5",
    id4:"4",
    idx:"×",
    id3:"3",
    id2:"2",
    id1:"1",
    iddiv:"÷",
    id0:"0",
    idd:".",
    ide:"＝",
    screenData:"0",
    operaSymbo:{"＋":"+","－":"-","×":"*","÷":"/",".":"."},
    lastIsOperaSymbo:false,
    iconType:'waiting_circle',
    iconColor:'white',
    arr:[],
    logs:[]
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
  },
  onReady:function(){
    // 页面渲染完成
  },
  onShow:function(){
    // 页面显示
  },
  onHide:function(){
    // 页面隐藏
  },
  onUnload:function(){
    // 页面关闭
  },
  clickBtn:function(event){
    var id = event.target.id;
    if(id == this.data.idb){  //退格←
      var data = this.data.screenData;
      if(data == "0"){
          return;
      }
      data = data.substring(0,data.length-1);
      if(data == "" || data == "－"){
          data = 0;
      }
      this.setData({"screenData":data});
      this.data.arr.pop();
    }else if(id == this.data.idc){  //清屏C
      this.setData({"screenData":"0"});
      this.data.arr.length = 0;
    }else if(id == this.data.idt){  //正负号+/-
      var data = this.data.screenData;
      if(data == "0"){
          return;
      }
      var firstWord = data.charAt(0);
      if(firstWord == "+"){
        data = data.substr(1);
        this.data.arr.shift();
      }else{
        data = "－" + data;
        this.data.arr.unshift("－");
      }
      this.setData({"screenData":data});
    }else if(id == this.data.ide){  //等于＝
      var data = this.data.screenData; //用于计算
      var arr=data  //用于写入历史记录
      if(data == "0"){
          return;
      }

      var num = "";
      var listOperator = [];
      var optarr = [];
      for(let i of data){
        if(isNaN(i) == false || i == this.data.idd || i == this.data.idt){
          num += i;
        }else{
          listOperator.push(i);
          optarr.push(num);
          num = "";
        }
      }
      optarr.push(Number(num));
      var result = Number(optarr[0])*1;

      var coutoperator=0;
      var opct=listOperator.length -1 //运算符的个数

      //能计算运算符优先级
      /*for(var i=opct; i>=1; i--){
        if(listOperator[i]==this.data.idx){
          midvalue=Number(optarr[i])*Number(optarr[i+1]);
          optarr.splice(i,2,String(midvalue));
          listOperator.splice(i,1);
        }
        if(listOperator[i]==this.data.iddiv){
          midvalue=Number(optarr[i])/Number(optarr[i+1]);
          optarr.splice(i,2,String(midvalue));
          listOperator.splice(i,1)
        }
      } */

      for(var i=1; i<optarr.length; i++){
        
        if(listOperator[coutoperator] == this.data.idadd){
          result += Number(optarr[i]);
          coutoperator+=1
        }else if(listOperator[coutoperator] == this.data.idj){
          result -= Number(optarr[i]);
          coutoperator+=1;
        }else if(listOperator[coutoperator] == this.data.idx){
          result *= Number(optarr[i]);
          coutoperator+=1;
        }else if(listOperator[coutoperator] == this.data.iddiv){
          result /= Number(optarr[i]);
          coutoperator+=1;
        }
      
        
      }
      this.setData({"screenData":parseFloat((result).toFixed(10))});

      //存储历史记录
      this.data.logs.push(arr+"="+String(parseFloat((result).toFixed(10))));
      wx.setStorageSync("calclogs",this.data.logs);

      this.data.arr.length = 0;
      this.data.arr.push(result);
    } else if(id == this.data.idH){  //转换十六进制
      var n=Number(this.data.screenData);
      var nH=n.toString(16);
      this.setData({"screenData":"0x"+nH}); 
      this.data.logs.push(String(n)+"="+"0x"+nH);
      wx.setStorageSync("calclogs",this.data.logs);
      this.data.arr.length = 0;
    }else if(id == this.data.idO){   //转换八进制
      var m=Number(this.data.screenData);
      var mH=m.toString(8);
      this.setData({"screenData":mH+"(o)"});
      this.data.logs.push(String(m)+"="+mH+"(O)");
      wx.setStorageSync("calclogs",this.data.logs);
      this.data.arr.length = 0;
    }else if(id == this.data.idBt){   //转换二进制
      var Bt=Number(this.data.screenData);
      var BtS = Bt.toString(2);
      this.setData({"screenData":BtS + "B"});
      this.data.logs.push(String(Bt)+"="+BtS+"B");
      wx.setStorageSync("calclogs",this.data.logs);
      this.data.arr.length = 0;
    }else if(id == this.data.idsin){   //求sin
      var SN=Number(this.data.screenData);
      var SNS=Math.sin(SN);
      this.setData({"screenData":SNS});
    }else if(id == this.data.idcos){   //求cos
      var cn =Number(this.data.screenData);
      var cns=Math.cos(cn);
      this.setData({"screenData":cns});
    }else if(id == this.data.idtan){   //求tan
      var tn =Number(this.data.screenData);
      var tns=Math.tan(tn);
      this.setData({"screenData":tns});
    }else if(id == this.data.idasin){   //求asin
      var asn =Number(this.data.screenData);
      var asns=Math.cosh(asn);
      this.setData({"screenData":asns});
    }else if(id == this.data.idatan){   //求atan
      var atn =Number(this.data.screenData);
      var atns=Math.cosh(atn);
      this.setData({"screenData":atns});
    }

    else{
      if(this.data.operaSymbo[id]){ //如果是符号+-*/
        if(this.data.lastIsOperaSymbo || this.data.screenData == "0"){
          return;
        }
      }

      var sd = this.data.screenData;
      var data;
      if(sd == 0){
        data = id;
      }else{
        data = sd + id;
      }
      this.setData({"screenData":data});
      this.data.arr.push(id);

      if(this.data.operaSymbo[id]){
        this.setData({"lastIsOperaSymbo":true});
      }else{
        this.setData({"lastIsOperaSymbo":false});
      }
    }
  },

  history:function(){
    wx.navigateTo({
      url:'../history/history'
    })
  }
})