using UnityEngine;
using Mirror; // Import Mirror namespace

public class SimpleMovement : NetworkBehaviour // Inherit from NetworkBehaviour
{
    public float moveSpeed = 5f;                // Movement speed
    public GameObject bulletPrefab;             // Bullet prefab to instantiate
    public Transform bulletSpawnPoint;          // Where the bullet spawns
    public float bulletSpeed = 20f;             // Speed at which the bullet moves
    public KeyCode fireKey = KeyCode.Space;     // Key to press to fire the bullet

    void Update()
    {
        // Only allow the local player to control their character
        if (!isLocalPlayer)
            return;

        Move();

        // Check if the fire key is pressed
        if (Input.GetKeyDown(fireKey))
        {
            // Call the Command to spawn bullets on the server
            CmdSpawn_();
        }
    }

    void Move()
    {
        // Get input from WASD keys or arrow keys
        float moveX = Input.GetAxis("Horizontal"); // A/D or Left/Right arrow keys
        float moveZ = Input.GetAxis("Vertical");   // W/S or Up/Down arrow keys

        // Create a movement vector
        Vector3 movement = new Vector3(moveX, 0f, moveZ) * moveSpeed * Time.deltaTime;

        // Apply the movement to the game object
        transform.Translate(movement, Space.World);
    }

    // Command function to spawn and throw the object on the server
    [Command]
    void CmdSpawn_()
    {
        // Instantiate the bullet on the server
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawnPoint.position, bulletSpawnPoint.rotation);

        // Get the Rigidbody component from the bullet
        Rigidbody rb = bullet.GetComponent<Rigidbody>();

        if (rb != null)
        {
            // Apply force to the bullet to throw it forward
            rb.velocity = bulletSpawnPoint.forward * bulletSpeed;
            Debug.Log("AA");
        }

        // Spawn the bullet on all clients
        NetworkServer.Spawn(bullet, connectionToClient);
    }
}
