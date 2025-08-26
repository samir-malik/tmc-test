// api call to create user
async function createUser() {
  const formData = new FormData(form);
  const json_payload = JSON.stringify(Object.fromEntries(formData.entries()));
  try {
    const response = await fetch("http://127.0.0.1:8000/users/create", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: json_payload,
    });
    const user = await response.json();
    const html_result = `
      <p> <b> User Successfully Created: </b> </p>
      <ul>
        <li>User ID: ${user.id}</li>
        <li>First Name: ${user.first_name}</li>
        <li>Last Name: ${user.last_name}</li>
        <li>DOB: ${user.dob}</li>
        <li>Age: ${user.age}</li>
      </ul>
    `
    document.getElementById("parent-div").innerHTML =  html_result;
  } catch (e) {
    console.error(e);
  }
}

// only allow date from today to 150 years in the past
// only allow dates 150 year in the past
const todayDate =  new Date();
const maxDate = todayDate.toISOString().split("T")[0]
const minDate = (
    new Date(todayDate.getFullYear() - 150, todayDate.getMonth(), todayDate.getDate())
).toISOString().split("T")[0];
document.getElementById("dob").setAttribute("min", minDate);
document.getElementById("dob").setAttribute("max", maxDate);

