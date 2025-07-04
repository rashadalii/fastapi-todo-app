from fastapi import status

def test_create_task(client, test_user_token):
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "status": "New"
    }
    response = client.post(
        "/api/v1/user/task",
        json=task_data,
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "Test Task"
    assert response.json()["user_id"] == 1  

def test_get_user_tasks(client, test_user_token):
   
    task_data = {"title": "Test Task", "status": "New"}
    client.post(
        "/api/v1/user/task",
        json=task_data,
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    
    
    response = client.get(
        "/api/v1/user/tasks",
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Test Task"

def test_update_task(client, test_user_token):
    
    create_response = client.post(
        "/api/v1/user/task",
        json={"title": "Original Title", "status": "New"},
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    task_id = create_response.json()["id"]
    
    
    update_data = {"title": "Updated Title", "status": "In Progress"}
    response = client.patch(
        f"/api/v1/user/{task_id}",
        json=update_data,
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "Updated Title"
    assert response.json()["status"] == "In Progress"

def test_delete_task(client, test_user_token):
   
    create_response = client.post(
        "/api/v1/user/task",
        json={"title": "Task to delete", "status": "New"},
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    task_id = create_response.json()["id"]
    
   
    response = client.delete(
        f"/api/v1/user/{task_id}",
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Deleted"}
    
 
    get_response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert get_response.status_code == status.HTTP_404_NOT_FOUND