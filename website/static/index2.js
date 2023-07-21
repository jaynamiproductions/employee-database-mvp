function deleteCert(profileid) {
    fetch('/delete-field2', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/certificates";
    });
}