import apiClient from "../api/client";

export const getHealth = async () => {
  const response = await apiClient.get("/health");
  return response.data;
};