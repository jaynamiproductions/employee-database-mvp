function deleteTime(profileid) {
    fetch('/delete-field11', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/timekeeping";
    });
}