import './Nav.css';
import React from 'react';

function Nav() {
  return (
    <div>
      <nav>
          <ul>
            <li><a href="/">home</a></li>
            <li><a href="/books">books</a></li>
            <li><a href="/blog">blog</a></li>
            <li><a href="https://tools.williamgay.me">tools</a></li>
            <li><a href="https://github.com/williamgay25">github</a></li>
            <li><a href="https://twitter.com/williamgay25">twitter</a></li>
            <li><a href="https://www.linkedin.com/in/williamegay/">linkedin</a></li>
          </ul>
        </nav>
    </div>
  );
}

export default Nav;