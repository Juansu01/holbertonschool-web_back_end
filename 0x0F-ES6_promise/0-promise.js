function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        if (true) {
            resolve('True');
        } else {
            reject(new Error('Error'));
        }
    });
}

export default getResponseFromAPI;
