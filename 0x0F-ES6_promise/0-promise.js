function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        /* eslint-disable */
        if (true) {
            resolve('True');
        } else {
            reject(new Error('Error'));
        }
        /* eslint-enable */
    });
}

export default getResponseFromAPI;
