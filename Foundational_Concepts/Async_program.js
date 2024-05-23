// Callback
function fetchData(callback) {
    setTimeout(() => {
        callback('Datat received');
    }, 1000);
}

fetchData(data => console.log(data));

