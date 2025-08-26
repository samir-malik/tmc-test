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

// only allow dates in past
document.getElementById("dob").setAttribute(
 "max",
 new Date().toISOString().split("T")[0]
);