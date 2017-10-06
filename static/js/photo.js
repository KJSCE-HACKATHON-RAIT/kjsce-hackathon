(function() {
  var video = document.getElementById('video'),
      canvas = document.getElementById('canvas'),
      context = canvas.getContext('2d'),
      photo = document.getElementById('photo'),
      canvas1 = document.getElementById('canvas1'),
      context1 = canvas1.getContext('2d'),
      photo1 = document.getElementById('photo1'),
      id_image = document.getElementById('id_image'),
      vendorUrl = window.URL || window.webkitURL;
      
  

      navigator.getUserMedia = navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia;



if (navigator.getUserMedia) {
   navigator.getUserMedia({ audio: false, video: true },
      function(stream) {
         var video1 = document.querySelector('video');
         video1.srcObject = stream;
         video.onloadedmetadata = function(e) {
           video.play();
         };
      },
      function(err) {
         console.log("The following error occurred: " + err.name);
      }
   );
} else {
   console.log("getUserMedia not supported");
}

//video: { facingMode: { exact: "environment" } }

/*
  navigator.getMedia = navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia;

*/
/*
  MediaStreamTrack.getSources(gotSources);
  var constraints = {
  audio: {
    optional: [{sourceId: audioSource}]
  },
  video: {
    optional: [{sourceId: videoSource}]
  }
  };

  navigator.getUserMedia({
    video: true,
    audio: false
  }, function(stream){
    video.src = vendorUrl.createObjectURL(stream);
    video.play();
  },  function(error){
    //do something
  });*/
/*

  navigator.getMedia({
    video: true ,
    
    audio: false
  }, function(stream){
    video.src = vendorUrl.createObjectURL(stream);
    video.play();
  }, function(error){
    //do something
  });
*/
  
  //document.getElementsByName("image")[0].setAttribute("value", document.write('<img src="'+ imageData +'"/>'));
  
  //document.getElementsByName("image")[0].setAttribute("filename", 'index.png');
  //document.write('<img src="'+ imageData +'"/>');

  document.getElementById('capture').addEventListener('click', function(){
    context.drawImage(video, 0, 0);
    photo.setAttribute('src', canvas.toDataURL('image/png'));

    context1.drawImage(video, 0, 0, 400, 300 );
    photo1.setAttribute('src', canvas1.toDataURL('image/png'));
    //video.setAttribute('src', canvas.toDataURL('image/png'));
    //document.getElementsByName("image")[0].setAttribute("type", imageData);
    //image.setAttribute('type', imageData);
    //image.setAttribute('type', canvas.toDataURL('image/octet-stream'));
    var imageData = canvas.toDataURL('image/png');
    id_image.setAttribute('value', imageData);
    id_image.setAttribute('type', imageData);
    console.log(id_image);
    
    
//    video.stop();

    //var imgData = canvas.toDataURL('image/png');
    //image.setAttribute('type', canvas.toDataURL('image/png'))
    //var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");  // here is the most important part because if you dont replace you will get a DOM 18 exception.
    //window.location.href=image;
    console.log("captured called");

  });


  document.getElementById('Cart').addEventListener('click', function(){
    
    var opt12 = document.getElementById("opt123").value;
    document.getElementById(opt12).checked = true;
    
    

    //var imgData = canvas.toDataURL('image/png');
    //image.setAttribute('type', canvas.toDataURL('image/png'))
    //var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");  // here is the most important part because if you dont replace you will get a DOM 18 exception.
    //window.location.href=image;
    

  });

})();
