import React, { useState } from 'react';
import { Auth } from "aws-amplify";
import { FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";
import LoadButton from "../components/LoadButton";
import { useFormFields } from "../libs/hooksLib";

export default function Login(props) {
  const [isLoading, setIsLoading] = useState(false);
  
  // uses custom hook to handle form fields
  const [fields, handleFieldChange] = useFormFields({
    email: "",
    password: ""
  });

 // validates login form
  function validateForm() {
    return fields.email.length > 0 && fields.password.length > 0;
  }

  // logs user in through Cognito and redirects back to home
  async function handleSubmit(event) {
    event.preventDefault();
    setIsLoading(true);

    try {
      await Auth.signIn(fields.email, fields.password);
      props.userHasAuth(true);
      props.history.push("/");
    } catch (e) {
      alert (e.message);
      setIsLoading(false);
    }
  }

  // login form
  return (
    <div className="Login">
      <form onSubmit={handleSubmit}>
        <FormGroup controlId="email" bsSize="large">
          <ControlLabel>Email</ControlLabel>
          <FormControl
            autoFocus
            type="email"
            value={fields.email}
            onChange={handleFieldChange}
          />
        </FormGroup>
        <FormGroup controlId="password" bsSize="large">
          <ControlLabel>Password</ControlLabel>
          <FormControl
            type="password"
            value={fields.password}
            onChange={handleFieldChange}
          />
        </FormGroup>
        <LoadButton
          block
          type="submit"
          bsSize="large"
          isLoading={isLoading}
          disabled={!validateForm()}
        >
          Login
        </LoadButton>
      </form>
    </div>
  );

}
