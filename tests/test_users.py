from fastapi import status

def test_filter_tasks_by_status(client, test_user_token):
    
    tasks = [
        {"title": "Task 1", "status": "New"},
        {"title": "Task 2", "status": "In Progress"},
        {"title": "Task 3", "status": "Completed"}
    ]
    for task in tasks:
        client.post(
            "/api/v1/user/task",
            json=task,
            headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
        )
    
    # Filter by status
    response = client.get(
        "/api/v1/user/tasks/filter?status=In Progress",
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["status"] == "In Progress"

def test_mark_task_completed(client, test_user_token):
    
    create_response = client.post(
        "/api/v1/user/task",
        json={"title": "Task to complete", "status": "New"},
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    task_id = create_response.json()["id"]
    
    # Mark as completed
    response = client.patch(
        f"/api/v1/user/{task_id}/complete",
        headers={"Authorization": f"Bearer {test_user_token['access_token']}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "Completed"