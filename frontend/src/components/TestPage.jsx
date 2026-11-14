import React, { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api"

const TestPage = () => {
  const [profileInfo, setProfileInfo] = useState(null);

  const fetchProfileInfo = async () => {
    const resp = await fetch(`${API_URL}/profiles/me/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("access")}`
      }
    });

    const data = await resp.json();

    if (!resp.ok) {
      alert("An error occured!");
      return;
    }

    setProfileInfo(data[0]);
    console.log(data[0]);
  };

  useEffect(() => {
    fetchProfileInfo();
  }, []);

  return (
    <>
      <div>You're logged in!</div>
      <div>
        <h2>My profile info:</h2>
        <ul className="bg-green-400">
          <li>Bio: {profileInfo?.bio}</li>
          <li>Headline: {profileInfo?.headline}</li>
          <li>LinkedIn: {profileInfo?.linkedin_url}</li>
          <li>Location: {profileInfo?.location}</li>
          <li>Phone: {profileInfo?.phone}</li>
          <li>Website: {profileInfo?.website}</li>
        </ul>
      </div>
    </>
  );
};

export default TestPage;
