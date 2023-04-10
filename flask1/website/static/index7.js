function deleteHR(profileid) {
    fetch('/delete-field7', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/human-resources";
    });
}