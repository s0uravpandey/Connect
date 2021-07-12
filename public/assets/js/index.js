const signInWithGoogleButton = document.getElementById('signInWithGoogle');
const signInWithFacebookButton = document.getElementById('signInWithFacebook');

//firebase aunthentication
const auth = firebase.auth();

//Firebase Google Authentication
const signInWithGoogle = () => {
  const googleProvider = new firebase.auth.GoogleAuthProvider();

//Google SignIN PopUP and redirect page
  auth.signInWithPopup(googleProvider)
  .then(() => {
    window.location.assign('./home');
  })
  .catch(error => {
    console.error(error);
  })
}

signInWithGoogleButton.addEventListener('click', signInWithGoogle);


//Firebase Facebook Authentication
const signInWithFacebook = () => {
  const facebookProvider = new firebase.auth.FacebookAuthProvider();

//Google SignIN PopUP and redirect page
  auth.signInWithPopup(facebookProvider)
  .then(() => {
    window.location.assign('./home');
  })
  .catch(error => {
    console.error(error);
  })
}

signInWithFacebookButton.addEventListener('click', signInWithFacebook);
