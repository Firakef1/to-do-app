
const updateBtn = document.getElementById('update-btn');
const newTask = document.getElementById('new-task');
const newTime = document.getElementById('new-time');
const newDate = document.getElementById('new-date');
const updateForm = document.getElementById('update-form');


state = true;
updateBtn.addEventListener('click', () => {
    if (state) {
        newTask.className = ""
        newTime.className = ""
        newDate.className = ""
        state = false;
    } else {

        updateForm.submit();
        newTask.className = "none"
        newTime.className = "none"
        newDate.className = "none"
        state = true;}
})