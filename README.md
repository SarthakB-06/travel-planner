# Travel Planner

A comprehensive AI-powered travel planning assistant built with Google ADK (Agent Development Kit). This multi-agent system helps users discover dream destinations, find nearby places, and stay updated with travel news and events.

## Features

- **🏖️ Travel Inspiration**: Get personalized destination recommendations and activity suggestions
- **📍 Place Discovery**: Find nearby hotels, restaurants, cafes, and attractions
- **📰 Travel News**: Stay updated with current travel events and news
- **🌍 Location Search**: Comprehensive location search using OpenStreetMap data
- **🤖 Multi-Agent Architecture**: Specialized agents working together for optimal results

## Architecture

The system consists of multiple specialized agents:

- **Root Agent**: Main travel concierge that coordinates all travel planning activities
- **Inspiration Agent**: Helps users discover destinations and activities
- **Places Agent**: Finds nearby places based on user preferences
- **News Agent**: Provides travel news and event recommendations
- **Search Agent**: Handles web searches for current information

## Prerequisites

- Python 3.12 or higher
- Google ADK access
- Internet connection for search and location services

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd travel-planner
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Set up environment variables:
   - Create a `.env` file in the `travel_planner/` directory
   - Add your Google ADK configuration and API keys

## Usage

### Running with ADK Web Interface

Start the web interface to interact with your travel planner:

```bash
adk web travel_planner
```

This will launch a web interface where you can chat with the travel planning assistant.

### Example Interactions

- "I want to plan a trip to Paris for my honeymoon"
- "Find hotels near the Eiffel Tower"
- "What are the current travel events in Tokyo?"
- "Suggest some romantic destinations in Europe"
- "Find cafes and restaurants near Times Square"

## Project Structure

```
travel-planner/
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── travel_planner/
    ├── .env
    ├── agent.py              # Root agent definition
    ├── supporting_agents.py  # Specialized agents
    ├── tools.py             # Search and location tools
    └── __pycache__/
```

## Components

### Root Agent ([`agent.py`](travel_planner/agent.py))
The main travel concierge that orchestrates all travel planning activities using sub-agents.

### Supporting Agents ([`supporting_agents.py`](travel_planner/supporting_agents.py))
- **Inspiration Agent**: Travel destination and activity recommendations
- **Places Agent**: Location-based place discovery
- **News Agent**: Travel news and events

### Tools ([`tools.py`](travel_planner/tools.py))
- **Google Search Tool**: Web search capabilities for current information
- **Location Search Tool**: OpenStreetMap-based place discovery
- **Geocoding**: Convert addresses to coordinates and vice versa

## Dependencies

- **google-adk**: Google Agent Development Kit for building AI agents
- **geopy**: Geocoding and location services
- **python-dotenv**: Environment variable management
- **requests**: HTTP requests for external APIs

## Configuration

The system uses OpenStreetMap's free APIs for location services, requiring no additional API keys for basic functionality. However, you'll need to configure Google ADK credentials in your `.env` file.

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue on the GitHub repository.

---

**Note**: This project uses experimental Google ADK features that may change in future versions.