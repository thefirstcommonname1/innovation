var quill = new Quill('#editor-container', {
  modules: {
      toolbar: [
          ['bold', 'italic'],
          ['link', 'blockquote', 'code-block', 'image'],
          [{ list: 'ordered' }, { list: 'bullet' }]
      ]
  },
  theme: 'snow'
});

var form = document.querySelector('form');
form.onsubmit = function () {
  // Populate hidden form on submit
  var about = document.querySelector('input[name=about]');
  about.value = JSON.stringify(quill.getContents());

  console.log("Submitted", $(form).serialize(), $(form).serializeArray());

};