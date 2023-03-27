function deleteProfile(profileid) {
    fetch('/delete-field', {
    method: 'POST',
    body: JSON.stringify({ profileid: profileid})
    }).then((_res) => {
        window.location.href = "/";
    });
}