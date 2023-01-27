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
   const countValue = document.getElementById('if_form-TOTAL_FORMS').getAttribute('value')
    for(let i=0; i<countValue; i++){
      const ConstForm = document.getElementById('form-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })

function add_topbanner_new_form(){
  if(event){
    event.preventDefault()
  }
  const TotalFormCount = document.getElementById('id_topbanner-TOTAL_FORMS');
  const currentCount = parseInt(TotalFormCount.value);
  const CopyTarget = document.getElementById('topbanner-form-list');
  const EmptyFormEl = document.getElementById('empty-form-topbanner').cloneNode(true);
  EmptyFormEl.setAttribute('class', '');
  EmptyFormEl.setAttribute('id', `topbanner-${currentCount}`);
  const regex = RegExp('__prefix__', 'g');
  EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`)
  TotalFormCount.setAttribute('value', `${currentCount + 1}`)

  CopyTarget.append(EmptyFormEl)
}

$(document).ready(function (){
   const countValue = document.getElementById('id_topbanner-TOTAL_FORMS').getAttribute('value')
    console.log(countValue)
    for(let i=0; i<countValue; i++){
        console.log(i)
      const ConstForm = document.getElementById('topbanner-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })


function add_newsbanner_new_form(){
  if(event){
    event.preventDefault()
  }
  const TotalFormCount = document.getElementById('id_newsbanner-TOTAL_FORMS');
  const currentCount = parseInt(TotalFormCount.value);
  const CopyTarget = document.getElementById('newsbanner-form-list');
  const EmptyFormEl = document.getElementById('empty-form-newsbanner').cloneNode(true);
  EmptyFormEl.setAttribute('class', '');
  EmptyFormEl.setAttribute('id', `newsbanner-${currentCount}`);
  const regex = RegExp('__prefix__', 'g');
  EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`)
  TotalFormCount.setAttribute('value', `${currentCount + 1}`)

  CopyTarget.append(EmptyFormEl)
}

$(document).ready(function (){
   const countValue = document.getElementById('id_newsbanner-TOTAL_FORMS').getAttribute('value')
    for(let i=0; i<countValue; i++){
      const ConstForm = document.getElementById('newsbanner-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })


function delForm(id){
    console.log(parseInt(id.match(/\d+/)));
    document.querySelector('#'+id).setAttribute('class', 'd-none')
    document.getElementById(`id_form-${parseInt(id.match(/\d+/))}-DELETE`).setAttribute('checked', '')
}

function delTopBannerForm(id){
    console.log(parseInt(id.match(/\d+/)));
    document.querySelector('#'+id).setAttribute('class', 'd-none')
    document.getElementById(`id_topbanner-${parseInt(id.match(/\d+/))}-DELETE`).setAttribute('checked', '')
}

function delNewsBannerForm(id){
    console.log(parseInt(id.match(/\d+/)));
    document.querySelector('#'+id).setAttribute('class', 'd-none')
    document.getElementById(`id_newsbanner-${parseInt(id.match(/\d+/))}-DELETE`).setAttribute('checked', '')
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

$('input:file').change(function (e){
  console.log(e.target.files[0].name)
  document.getElementById('nameloadfile').innerText = e.target.files[0].name
})

function switchList(radiotype){
    var choose_model = document.getElementById('select_user_mailing')

    if(radiotype.id === 'id_all_user'){
        document.getElementById('id_select_user').checked = false
        document.getElementById('id_all_user').value = 'all_user'
        choose_model.setAttribute('class', 'd-none')
    } else {
        document.getElementById('id_all_user').checked = false
        document.getElementById('id_select_user').value = 'check_user'
        choose_model.setAttribute('class', 'btn_width btn_add rounded')
    }
}

function name_load_template(name){
    document.getElementById('file_name_template').innerText =
        name.value

}


$(document).ready(function () {
        $('#choose_table').DataTable({
            columnDefs: [
                { targets: 'no-sort', orderable: false }
            ],
            lengthMenu: [5, 10, 15, 20, 50],
            language: {
                "emptyTable": "В таблиці немає записів",
                info: "Показувати від _START_ до _END_ из _TOTAL_ записів",
                infoEmpty: "Showing 0 to 0 of 0 entries",
                lengthMenu: "Показувати _MENU_ записів",
                search: "Пошук:",
                paginate: {
                   sNext: 'Вперед',
                   sPrevious: 'Назад',
                   sFirst: 'Перша',
                   sLast: 'Остання'
                }
            }
        });
    });

function back_type(back){
    if(back.id === 'id_back_0'){
        document.getElementById('id_back_1').checked = false;
        document.getElementById('id_back_1').value = '#000000';
        document.getElementById('id_back_type_img').checked = true;

        document.getElementById('picker_back').setAttribute('class', 'd-none')
        document.getElementById('id_back_image').setAttribute('class', 'ml-5')
    } else {
        document.getElementById('id_back_0').checked = false;
        document.getElementById('id_back_image').setAttribute('class', 'd-none');
        document.getElementById('picker_back').setAttribute('class', 'ml-3 mt-3');
        document.getElementById('id_back_type_img').checked = false;
    }
}

function changepicker(){
    document.getElementById('id_back_type_pick').value = document.getElementById('picker-color').value
    console.log(document.getElementById('picker-color').value)
}


