function deleteNewhires(profileid) {
    fetch('/delete-field9', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/new-hires";
    });
}