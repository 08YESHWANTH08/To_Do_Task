const todoIuput=document.querySelector('.todo-input');
const todoButton=document.querySelector('.todo-button');
const todoList=document.querySelector('.todo-list');
const filterOption=document.querySelector('.filter-todo');

todoButton.addEventListener('click',addTodo);
todoList.addEventListener('click',deleteCheck);
filterOption.addEventListener('click',filterTodo);
function addTodo(event){
    event.preventDefault();

    const todoDiv= document.createElement('div');
    todoDiv.classList.add("todo");

    const newTodo=document.createElement('current');
    newTodo.innerText= todoIuput.value;
    newTodo.classList.add('todo-item');
    todoDiv.appendChild(newTodo);



    const completedButton=document.createElement('button');
    completedButton.innerHTML='<i style="font-size:1.5rem" class="fa fa-check" aria-hidden="true"></i>';
    completedButton.classList.add("complete-btn");
    todoDiv.appendChild(completedButton);

    const trashButton=document.createElement('button');
    trashButton.innerHTML='<i style="font-size:1.5rem" class="fa fa-trash" aria-hidden="true"></i>';
    trashButton.classList.add("trash-btn");
    todoDiv.appendChild(trashButton); 
    
    todoList.appendChild(todoDiv);
    todoIuput.value="";
}
function deleteCheck(event){
    const item=event.target;
    if(item.classList[0]==='trash-btn'){
        const todo=item.parentElement;
        todo.remove();
    }
    if(item.classList[0]==='complete-btn'){
        const completed_items=item.parentElement;
        completed_items.classList.toggle('completed');    
    }
}
function filterTodo(e) {
    const todos=todoList.childNodes;
    todos.forEach(function(todo){
        switch(e.target.value){
            case "all":
                todo.style.display="flex";break;
            case "completed":
                if (todo.classList.contains("completed")){
                    todo.style.display="flex";
                }
                else{
                    todo.style.display="none";
                }
                break;
            case "uncompleted":
                if(! todo.classList.contains('completed')){
                    todo.style.display="flex";
                }
                else{
                    todo.style.display="none";
                }
                break;
        }
    });
}