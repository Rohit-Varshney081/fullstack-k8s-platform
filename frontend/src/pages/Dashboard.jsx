import { useEffect, useState } from "react";
import { getHealth } from "../services/healthService";

function Dashboard() {
  const [health, setHealth] = useState("");

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await getHealth();
        setHealth(data.status);
      } catch (error) {
        console.error(error);
      }
    };

    loadData();
  }, []);

  return (
    <>
      <h1>FullStack Platform</h1>

      <p>Backend Status: {health}</p>
    </>
  );
}

export default Dashboard;