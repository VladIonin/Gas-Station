document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault();
    loadData();
});

document.getElementById('stationInfo').addEventListener('submit', function (event) {
    event.preventDefault();
    saveChanges();
});

function validateStationId(stationId) {
    const id = parseInt(stationId, 10);
    return !isNaN(id) && id >= 1 && id <= 99;
}

function loadData() {
    const stationId = document.getElementById('stationId').value;

    if (!validateStationId(stationId)) {
        alert('В поле ID принимаются значения от 1 до 99.');
        return;
    }

    fetch(`http://127.0.0.1:8080/getStationInfo?id=${stationId}`)
        .then(response => {
            if (response.status === 404) {
                // Station not found, clear input fields and display a message
                document.getElementById('stationTitle').innerText = `АЗС №${stationId} не найдена - создайте новую запись`;
                clearInputFields();
                document.getElementById('stationInfo').style.display = 'block';
            } else if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            } else {
                // Station exists, populate fields with received data
                return response.json();
            }
        })
        .then(data => {
            if (data) {
                document.getElementById('stationTitle').innerText = `Управление АЗС №${data.station.station_id}`;
                document.getElementById('address').value = data.station.address;
                document.getElementById('price92').value = data.data[0].price;
                document.getElementById('amount92').value = data.data[0].amount;
                document.getElementById('price95').value = data.data[1].price;
                document.getElementById('amount95').value = data.data[1].amount;
                document.getElementById('price98').value = data.data[2].price;
                document.getElementById('amount98').value = data.data[2].amount;
                document.getElementById('priceDT').value = data.data[3].price;
                document.getElementById('amountDT').value = data.data[3].amount;

                document.getElementById('stationInfo').style.display = 'block';
            }
        })
        .catch(error => console.error('Error:', error));
}

function clearInputFields() {
    document.getElementById('address').value = '';
    document.getElementById('price92').value = '';
    document.getElementById('amount92').value = '';
    document.getElementById('price95').value = '';
    document.getElementById('amount95').value = '';
    document.getElementById('price98').value = '';
    document.getElementById('amount98').value = '';
    document.getElementById('priceDT').value = '';
    document.getElementById('amountDT').value = '';
}

function saveChanges() {
    const stationId = document.getElementById('stationId').value;
    const address = document.getElementById('address').value;
    const price92 = document.getElementById('price92').value;
    const amount92 = document.getElementById('amount92').value;
    const price95 = document.getElementById('price95').value;
    const amount95 = document.getElementById('amount95').value;
    const price98 = document.getElementById('price98').value;
    const amount98 = document.getElementById('amount98').value;
    const priceDT = document.getElementById('priceDT').value;
    const amountDT = document.getElementById('amountDT').value;

    const data = {
        id: stationId,
        address: address,
        data: [
            {fuel: '92', price: price92, amount: amount92},
            {fuel: '95', price: price95, amount: amount95},
            {fuel: '98', price: price98, amount: amount98},
            {fuel: 'Disel Fuel', price: priceDT, amount: amountDT}
        ]
    };

    fetch('http://127.0.0.1:8080/setStation/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(result => console.log('Success:', result))
        .catch(error => console.error('Error:', error));
}