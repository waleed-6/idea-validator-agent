from agent import StartupValidatorAgent

def main():
    print("🚀 Startup Idea Validator Agent")
    idea = input("\n💡 Describe your startup idea: ")

    agent = StartupValidatorAgent()
    report = agent.run(idea)

    print("\n📄 Validation Report:\n")
    print(report)

if __name__ == "__main__":
    main()
