import * as React from 'react';
import SignIn from './components/SignUp';
import ButtonAppBar from './components/AppBar';

function App() {
  return (
    <div className="App">
      <ButtonAppBar />
      <SignIn />
    </div>
  );
}

export default App;
