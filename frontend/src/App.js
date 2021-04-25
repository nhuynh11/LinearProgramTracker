import React, { Component } from "react";

const Programs = [
  {
    id: 1,
    program_type: "SP",
    start_date: "2021-04-25T06:48:07",
    resets: 0
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      programList: Programs,
    };
  }

  renderPrograms = () => {
    const activePrograms = this.state.programList;

    return activePrograms.map((program) => (
      <li key={program.id} className="list-group-item d-flex justify-content-between align-items-center">
        <span>
          {program.program_type}
        </span>
        <span>
          {program.start_date}
        </span>
      </li>
    ));
  }

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush border-top-0">
                {this.renderPrograms()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }

  
}

export default App;