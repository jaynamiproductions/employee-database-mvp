function deleteForm(profileid) {
    fetch('/delete-forms', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/forms";
    });
}