$(function (){
    $('#datepicker1').datepicker({dateFormat: 'dd/mm/yy'});
});

function addLogoImage(input, img) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = function (e) {
      $('#'+img).attr('src', e.target.result).width(170).height(250);
    };

    reader.readAsDataURL(input.files[0]);
  }
}

function addPhotoImage(input, img) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = function (e) {
      $('#'+img).attr('src', e.target.result).width(300).height(200);
    };

    reader.readAsDataURL(input.files[0]);
  }
}

function add_new_form(){
  if(event){
    event.preventDefault()
  }
  const TotalFormCount = document.getElementById('id_form-TOTAL_FORMS');
  const currentCount = parseInt(TotalFormCount.value);
  console.log(currentCount)
  const CopyTarget = document.getElementById('gallery-form-list');
  const EmptyFormEl = document.getElementById('empty-form').cloneNode(true);
  EmptyFormEl.setAttribute('class', '');
  EmptyFormEl.setAttribute('id', `form-${currentCount}`);
  const regex = RegExp('__prefix__', 'g');
  EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`)
  TotalFormCount.setAttribute('value', `${currentCount + 1}`)

  CopyTarget.append(EmptyFormEl)
}


$(document).ready(function (){
   const countValue = document.getElementById('id_form-TOTAL_FORMS').getAttribute('value')
    for(let i=0; i<countValue; i++){
      const ConstForm = document.getElementById('form-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })


function delForm(id){
    console.log(parseInt(id.match(/\d+/)));
    document.querySelector('#'+id).setAttribute('class', 'd-none')
    document.getElementById(`id_form-${parseInt(id.match(/\d+/))}-DELETE`).setAttribute('checked', 'true')
}



function deleteImage(img){
  document.querySelector('#'+img).setAttribute('src', '/static/dist/img/logo-spider.jpg');
}

function getCurrentURL(){
  return window.location.href
}
$(document).ready(function (){
var url = window.location.href;
if (url.includes('uk')){
  document.getElementById('id_uk').setAttribute('class', 'nav-link fw-normal active')
  document.getElementById('id_uk_tabs')

}else{
  document.getElementById('id_en').setAttribute('class', 'nav-link fw-normal active')
  document.getElementById('id_uk_tabs').setAttribute('class', 'd-none')
  document.getElementById('id_en_tabs').setAttribute('class', 'tab-pane fade active show')
}});


$(document).ready(function (){
  document.getElementById('id_language_0').setAttribute('class', 'd-none');
  document.getElementById('id_sex_0').setAttribute('class', 'd-none')
});

// function confirmfunc(){
//   let answer = confirm('Ви впевнені ?');
//   if(answer = true){
//     $('.delete-image').cancel()
//   }else{
//
//   }
// }
