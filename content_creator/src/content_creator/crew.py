from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from content_creator.tools.browser_tools import BrowserTools
from content_creator.tools.search_tools import SearchTools
from crewai import LLM





search_tool = SearchTools()
browser_tool = BrowserTools()

#uses Ollama
llm = LLM(
    model="ollama/qwen2.5:14b",
    base_url="http://localhost:11434"
)

# uses Gemini 
# llm = LLM(
#     model="gemini-1.5-flash-latest",
#     temperature=0.8
# )

@CrewBase
class ContentCreator():
    """ContentCreator crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def product_competitor_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['product_competitor_researcher'],  
            verbose=True,
            tools = [search_tool,browser_tool],
            llm=llm
        )

    @agent
    def strategy_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_planner'],  
            verbose=True,
            tools = [search_tool],
            llm=llm
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],  
            verbose=True,
            llm=llm
        )

    @agent
    def senior_photographer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_photographer'],  
            verbose=True,
            llm=llm
        )

    @agent
    def chief_creative_director(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_creative_director'],  
            verbose=True,
            llm=llm
        )

    @agent
    def adapter(self) -> Agent:
        return Agent(
            config=self.agents_config['adapter'],  
            verbose=True,
            llm=llm
        )

    @agent
    def ab_variant_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['ab_variant_generator'],  
            verbose=True,
            llm=llm
        )

    @task
    def website_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['website_analysis'],  
        )

    @task
    def market_anaysis(self) -> Task:
        return Task(
            config=self.tasks_config['market_anaysis'],  
        )

    @task
    def campaign_develpoment(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_develpoment'],  
        )

    @task
    def write_copy(self) -> Task:
        return Task(
            config=self.tasks_config['write_copy'],  
        )
    
    @task
    def ab_variant_task(self) -> Task:
        return Task(
            config=self.tasks_config['ab_variant_task'],  
            tools = [search_tool]
        )


    @task
    def take_photo(self) -> Task:
        return Task(
            config=self.tasks_config['take_photo'],  
        )

    @task
    def approval_photo(self) -> Task:
        return Task(
            config=self.tasks_config['approval_photo'],  
        )

    @task
    def adapter_task(self) -> Task:
        return Task(
            config=self.tasks_config['adapter_task'],  
            output_file="output/final_platform_content.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ContentCreator Crew """

        # manager = Agent(
        #     config =self.agents_config['manager'],
        #     allow_delegation = True,
        #     verbose=True,
        #     llm = llm,
        #     max_iter=8
        # )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            # manager_agent= manager,
            verbose=True    
        )