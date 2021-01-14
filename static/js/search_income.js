const searchfield = document.querySelector("#searchfield")
const tableoutput =  document.querySelector(".table-output")
const tablenoresults =  document.querySelector(".no-results")
const apptable =  document.querySelector(".app-table")
const pagination =  document.querySelector(".pagination")
const tbody =  document.getElementById("tbody")

tablenoresults.style.display = "none";
tableoutput.style.display = "none";
apptable.style.display = "block";
pagination.style.display = "block";

searchfield.addEventListener('keyup', (e) => {
    tbody.innerText = " ";
    const  searchvalue = e.target.value;
    if (searchvalue.trim().length > 0){
      pagination.style.display = "none";
      tbody.innerHTMl="";
      fetch ("/search_incomes",{
        body: JSON.stringify({ searchedText: searchvalue.trim() }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data)
            apptable.style.display = "none";
            tableoutput.style.display = "block";
            pagination.style.display = "none";

        if (data.length===0){
            tablenoresults.innerHTML = `<p> No results </p>`
            console.clear()
        }else{

            for (var i=0; i<data.length; i++) {
                var item = data[i];
//            data.forEach((item) => {
                tbody.innerHTML +=`
                <tr>
                    <td>${item.amount}</td>
                    <td>${item.source_name}</td>
                    <td>${item.income_name}</td>
                    <td>${item.date_added}</td>
                    <td>
                        <a href="edit_income/${item.id}" class="btn btn-success btn-sm rounded-0" type="button" data-toggle="tooltip" data-placement="top" title="Edit"><i class="fa fa-edit"></i></a>
                        <a href="delete_income/${item.id}" class="btn btn-danger btn-sm rounded-0" type="button" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash"></i></a>
                    </td>
                </tr>`
            };
        }
        });
    }else{
        tablenoresults.style.display = "block";
        tableoutput.style.display = "none";
        apptable.style.display = "block";
        pagination.style.display = "block";
    }
});