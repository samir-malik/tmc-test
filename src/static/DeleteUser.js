// api call to delete users
async function deleteUser(button_id) {
    const user_id = button_id.split("-")[1]
    const row_id = `row-${user_id}`
    try {
      await fetch(`http://127.0.0.1:8000/user/${user_id}/delete/`, {
        method: "DELETE",
      });
        if (document.getElementById("user-table").rows.length == 2){
            noUsers()
        }else{
            document.getElementById(row_id).remove();
        }
    } catch (e) {
      console.error(e);
    }
}