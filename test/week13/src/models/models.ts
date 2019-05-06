export interface TaskList {
    id: number;
    name: string;
}

export interface Course {
    id: number;
    name: string;
    description: string;
}

export interface Task {
    id: number;
    name: string;
    created_at: string;
    due_on: string;
    status: string;
}

export interface IAuthResponse {
    token: string;
  }