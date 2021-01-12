const searchfield = document.querySelector("#searchfield")
const tableoutput =  document.querySelector(".table-output")
const apptable =  document.querySelector(".app-table")
const pagination =  document.querySelector(".pagination")
const tbody =  document.querySelector(".tbody")
tableoutput.style.display = "none";


searchfield.addEventListener('keyup', (e) => {
    const  searchvalue = e.target.value;
    if (searchvalue.trim().length > 0){
      pagination.style.display = "none";
      tbody.innerHTMl=" ";
      fetch ("/search_expenses",{
        body: JSON.stringify({ searchedText: searchvalue }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data)
            apptable.style.display = "none";
            tableoutput.style.display = "block";

        if (data.length===0){
            tableoutput.innerHTML = "No results"
        }else{

            data.forEach((item) => {
                tbody.innerHTML+=`
                <tr>
                    <td>${item.amount}</td>
                    <td>${item.category_name}</td>
                    <td>${item.expense_name}</td>
                    <td>${item.date_added}</td>
                </tr>
            `
            })
        }
        });
    }else{
        tableoutput.style.display = "none";
        apptable.style.display = "block";
        pagination.style.display = "block";
    }
});