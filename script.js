document.addEventListener('DOMContentLoaded', function () {
    loadTasks();
});

function loadTasks() {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';

    // Retrieve tasks from local storage
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    tasks.forEach(function (task) {
        createTaskElement(task);
    });
}

function addTask() {
    const taskInput = document.getElementById('task-input');
    const taskText = taskInput.value.trim();

    if (taskText !== '') {
        // Retrieve tasks from local storage
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

        // Add new task
        tasks.push(taskText);

        // Save tasks to local storage
        localStorage.setItem('tasks', JSON.stringify(tasks));

        // Create task element and append to the list
        createTaskElement(taskText);

        // Clear the input field
        taskInput.value = '';
    }
}

function createTaskElement(taskText) {
    const taskList = document.getElementById('task-list');

    const li = document.createElement('li');
    const span = document.createElement('span');
    span.textContent = taskText;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.className = 'delete-btn';
    deleteButton.addEventListener('click', function () {
        deleteTask(taskText);
    });

    li.appendChild(span);
    li.appendChild(deleteButton);

    taskList.appendChild(li);
}

function deleteTask(taskText) {
    // Retrieve tasks from local storage
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    // Remove the task
    tasks = tasks.filter(task => task !== taskText);

    // Save updated tasks to local storage
    localStorage.setItem('tasks', JSON.stringify(tasks));

    // Reload the task list
    loadTasks();
}
