import React from 'react';

import onlineIcon from '../../icons/onlineIcon.png';

import './TextContainer.css';

const TextContainer = ({ users }) => (
  <div className="textContainer">
    <div>
      <h1>Connect<span role="img" aria-label="emoji">💬</span></h1>
      <a href="https://trial-1f73d.web.app/home.html"><button className="btnprimary">Home</button></a>
      <a href=""><button className="leavechat btnprimary">Leave</button></a>
    </div>
    {
      users
        ? (
          <div>
            <h1>People Online:</h1>
            <div className="activeContainer">
              <h2>
                {users.map(({name}) => (
                  <div key={name} className="activeItem">
                    {name}
                    <img alt="Online Icon" src={onlineIcon}/>
                  </div>
                ))}
              </h2>
            </div>
          </div>
        )
        : null
    }
  </div>
);

export default TextContainer;