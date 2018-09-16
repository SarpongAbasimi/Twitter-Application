document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('.nav-img').onclick =() =>{
    const show = document.querySelector('.list-container');
    if(show.style.display=='none'){
      show.style.display='block';
    }
    else{
      show.style.display='none';
    }
  }
});
