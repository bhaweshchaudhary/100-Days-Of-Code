document.querySelector('#push').onclick = function() {
    // Adding Validation for Empty input field
    if(document.querySelector('#newtask input').value.length == 0) {
        alert('Please Enter a Task')
    }
    // Adding a new task
    else {
        document.querySelector('#tasks').innerHTML += `
            <div class="task">
                <span id="taskname">
                    ${document.querySelector('#newtask input').value}
                </span>
                <button class="delete">
                    <i class="fa-solid fa-trash"></i>
                </button>
            </div>
        `;
    var current_tasks = document.querySelectorAll(".delete");
    for(var i=0; i<current_tasks.length; i++) {
        current_tasks[i].onclick = function() {
            this.parentNode.remove();
        }
    }
    // crossing off a completed task
    var tasks = document.querySelectorAll(".task");
    for(var i=0; i<tasks.length; i++) {
        tasks[i].onclick = function() {
            this.classList.toggle("completed");
        }
    }
    // clearing the input field after each entry
    document.querySelector("#newtask input").value = "";
    }
}