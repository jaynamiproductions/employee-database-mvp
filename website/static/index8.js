function deleteLabor(profileid) {
    fetch('/delete-field8', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/labor-relations";
    });
}