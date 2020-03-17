import React, { useState, useEffect } from "react";
import { Link, withRouter } from "react-router-dom";
import { Navbar, Nav, NavItem } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import './App.css';
import Routes from "./Routes";
import { Jumbotron } from "./components/Jumbotron";
import { Auth } from "aws-amplify";

function App(props) {
  const [isAuth, userHasAuth] = useState(false);
  const [isAuthenticating, setIsAuthenticating] = useState(true);

  // triggers onLoad the first time app is loaded
  useEffect(() => {
    onLoad();
  }, []);

  // checks browser cache to see if user is already signed in
  async function onLoad() {
    try {
      await Auth.currentSession();
      userHasAuth(true);
    }
    catch(e) {
      if (e !== 'No current user') {
        alert(e);
      }
    }

    setIsAuthenticating(false);
  }

  // logs out user
  async function handleLogout() {
    await Auth.signOut();
    userHasAuth(false);
    props.history.push("/login");
  }

  return (
    !isAuthenticating &&
    <div className="App container">
      <Navbar fluid collapseOnSelect>
        <Navbar.Header>
          <Navbar.Brand>
            <Link to="/">Ramblerfy</Link>
          </Navbar.Brand>
        </Navbar.Header>
        <Nav>
          {isAuth
            ? <NavItem onClick={handleLogout}>Logout</NavItem>
            : <>
                <LinkContainer to="/signup">
                  <NavItem>Signup</NavItem>
                </LinkContainer>
                <LinkContainer to="/login">
                  <NavItem>Login</NavItem>
                </LinkContainer>
              </>
          }
        </Nav>
      </Navbar>
      <Jumbotron />
      { /*this handles all components rendered under the navbar/jumbo */ }
      <Routes appProps={{ isAuth, userHasAuth }} />
    </div>
  );
}

export default withRouter(App);
