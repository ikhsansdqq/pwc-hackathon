'use client'

import React, {useState, useEffect} from 'react';
import axios from 'axios';

export default function App() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/users').then(response => {
            setUsers(response.data)
        });
    }, []);
    return (

        <main className="md:my-6 xl:max-w-3xl mx-auto">
            <h1 className="text-4xl font-bold dark:text-white mb-3">Retrieval from Flask Server</h1>
            <p className="dark:text-gray-300 mb-3">Endpoint located at: <em
                className="underline"><a href="http://localhost:5000/users">http://localhost:5000/users</a></em></p>
            {users.map(user => (
                <li className="dark:text-white list-inside" key={user.id}>{user.id}. {user.name} <a
                    href={user.email}>{user.email}</a></li>
            ))}
        </main>
    )
}