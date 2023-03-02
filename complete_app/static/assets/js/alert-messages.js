function alertMessageGet() {
    inputIdTarefa = document.getElementsByTagName('input')[0];

    if (inputIdTarefa.value === '') {
        window.alert('Nenhum Id inserido.');
    }
}

function alertMessagePost() {
    inputResponsavel = document.getElementsByTagName('input')[0];
    inputTarefa = document.getElementsByTagName('input')[1];
    inputStatus = document.getElementsByTagName('input')[2];

    if (inputResponsavel.value === '' || inputTarefa.value === '' || inputStatus.value === '' ) {
        window.alert('Responsável, Tarefa ou Status não inseridos.');
    } else {
        window.alert('Tarefa incluída!');
    }
}

function alertMessagePut() {
    inputIdTarefa = document.getElementsByTagName('input')[0];
    inputStatus = document.getElementsByTagName('input')[1];

    if (inputIdTarefa.value === '' || inputStatus.value === '') {
        window.alert('Id ou Status não inseridos.');
    }
}

function alertMessageDelete() {
    inputIdTarefa = document.getElementsByTagName('input')[0];

    if (inputIdTarefa.value === '') {
        window.alert('Nenhum Id inserido.');
    }
}
