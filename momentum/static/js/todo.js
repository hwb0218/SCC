const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos";

const toDos = [];

function deleteToDo(event){
	const btn = event.target;
	const li = btn.parentNode;
	toDoList.removeChild(li);
	const cleanToDos = toDos.filter(function(toDo){
		return toDo.id !== parseInt(li.id);
	});
	console.log(cleanToDos);


function saveToDos(){
	localStorage.setItem(TODOS_LS, JSON.stringify(toDos)) // localStorage.setItem(key,value)
}

function paintToDo(value) {
	const li = document.createElement("li");
	const delBtn = document.createElement("button");
	const span = document.createElement("span");
	const newId = toDos.length + 1;
	delBtn.innerText = "❌";
	delBtn.addEventListener("click", deleteToDo);
	span.innerText = value;
	li.appendChild(span);
	li.appendChild(delBtn);
	li.id = newId;
	toDoList.appendChild(li);
	const toDoObj = {
		text : value,
		id : newId
	};
	toDos.push(toDoObj);
	saveToDos();
}
function handleSubmit(event){
	event.preventDefault();
	const currentValue = toDoInput.value;
	paintToDo(currentValue);
	toDoInput.value = "";
}

// function something(toDo){
// 	paintToDo(toDo.text);
// };

function loadToDos(){
	const loadedToDos = localStorage.getItem(TODOS_LS);
	if(loadedToDos !== null) {
		const parsedToDos = JSON.parse(loadedToDos);
		parsedToDos.forEach(function(toDo){ // 이함수의 동작은 어떤식?
			paintToDo(toDo.text);
		});
	}
}

function init() {
	loadToDos();
	toDoForm.addEventListener("submit", handleSubmit);
}
init();