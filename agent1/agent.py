# hello world agent

from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

class AgentState(TypedDict):
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """
    Simple node than adds greeting message to the state
    """
    state["message"] = f"Hey, {state['message']}, how is it going"
    return state

graph = StateGraph(
    AgentState,
)

graph.add_node('greeter', greeting_node)
graph.set_entry_point('greeter')
graph.set_finish_point('greeter')


app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

result = app.invoke({"message": 'Bob'})
print(result)