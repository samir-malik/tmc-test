  // api call to get users and create table
    async function getUsers() {
        try {
            const data = await fetch("http://127.0.0.1:8000/users/", {
                method: "GET",
            });
            const users = await data.json();

            // populate table if we have users
            if (users.length != 0){

                let table_headers = `
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">DOB</th>
                        <th scope="col">Age</th>
                        <th scope="col">Delete</th>
                     </tr>
                `

                let table_entries = ""
                users.forEach(function (user) {
                    table_entries += `
                        <tr id="row-${user.id}">
                          <th scope="row">${user.id}</th>
                          <td>${user.first_name}</td>
                          <td>${user.last_name}</td>
                          <td>${user.dob}</td>
                          <td>${user.age}</td>
                          <td>
                              <button id="button-${user.id}" class="btn danger" onclick="deleteUser(this.id)">
                                <i class="material-icons" style="font-size:18px;color:red">delete</i>
                             </button>
                          </td>
                        </tr>
                `
            })
            document.getElementById('thead').innerHTML = table_headers
            document.getElementById('tbody').innerHTML = table_entries

            }else{
                noUsers()
            }

        } catch (e) {
            console.error(e);
        }
    }