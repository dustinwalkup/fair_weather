document.addEventListener('DOMContentLoaded', function(){
const table = document.querySelector("tbody")
const rows = table.getElementsByTagName('tr');

for (let row of rows){
    let required_temp = Number(row.querySelector(".required_temp").innerHTML.slice(0,-3))
    let current_temp = Number(row.querySelector(".current_temp").innerHTML.slice(0,-3))
    if (current_temp >= required_temp) row.classList.add("table-green")
    else row.classList.add("table-red")

}
}, false);

function pulsar(obj) {
  obj.value=obj.value.toUpperCase();
}