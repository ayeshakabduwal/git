
//takes the note id and sends a post request to the delete npte endpoint 
//after it gets a response, it reloads the window and redirects to the home page 
function deleteNote(noteId){
    fetch('delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href='/';
    }); 
}