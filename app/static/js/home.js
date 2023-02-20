function renderPicture() {}

function renderMasonry() {

}

function getPictureList() {
    const url = `https://api.kevinjobs.com:5000/v2/pictures?offset=0&limit=999&orderBy=createAt&order=desc`;
    fetch(url, {
        method: 'get',
    }).then(resp => {
        console.log(resp);
        return resp.json();
    }).then(json => {
        console.log("hello");
        console.log(json);
    })
}