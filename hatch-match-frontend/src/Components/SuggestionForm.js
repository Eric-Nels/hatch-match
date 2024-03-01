import React, { useState } from 'react';
import axios from 'axios';

const SuggestionForm = () => {
    const [name, setName] = useState('');
    const [image, setImage] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('name', name);
        formData.append('image', image);

        try {
            await axios.post('http://localhost:5000/api/submit', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            // Redirect or show a success message
        } catch (error) {
            console.error('Error submitting suggestion:', error);
            // Handle error
        }
    };

    const handleImageChange = (e) => {
        setImage(e.target.files[0]);
    };

    return (
        <div>
            <h2>Suggestion Box</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Suggestion Name:</label><br />
                <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)} /><br /><br />
                <label htmlFor="image">Upload Image:</label><br />
                <input type="file" id="image" name="image" onChange={handleImageChange} /><br /><br />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default SuggestionForm;